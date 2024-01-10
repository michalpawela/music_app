import {useNavigate, useParams} from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { DetailsHeader, Error, Loader, RelatedSongs } from "../components";

import { setActiveSong, playPause } from "../redux/features/playerSlice";
import {
  useGetSongDetailsQuery,
  useGetSongRelatedQuery,
} from "../redux/services/shazamCore";
import useGetSong from "../hooks/song/useGetSong";
import PlaylistCard from "../components/PlaylistCard";
import React, {useState} from "react";
import useGetAllPlaylists from "../hooks/playlist/useGetAllPlaylist";
import useGetAllPlaylist from "../hooks/playlist/useGetAllPlaylist";
import axios from "axios";

const SongDetails = () => {
  const dispatch = useDispatch();
  const navigator = useNavigate();
  const { songid } = useParams();
  const { activeSong, isPlaying } = useSelector((state) => state.player);
  const { song,loading} = useGetSong(songid)
  const {playlists} = useGetAllPlaylist();
  const [playlistId, setPlaylistId] = useState(1)
  const [success, setSuccess] = useState(false)
  const [error, setError] = useState(false)

  const handleSubmitForm = async (event) => {
    event.preventDefault();

    const requestData = {
      PlaylistID: playlistId,
      SongID: songid,
    };

    try{

      const response = await axios.post('http://127.0.0.1:5000/playlists/add_song', requestData, {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        }
      });

      if (!response.data || response.status !== 200) {
        throw new Error('Failed to add a new song');
      }

      setSuccess(true);

      setTimeout(() => {
        setSuccess(false);
        navigator('/playlists')

      }, 2000);



    } catch (e) {
      console.error(e);
      setError(true);
    } finally {

    }

  }


  if (loading) {
    return <Loader title="Searching song details" />;
  }

  if (error) return <Error />;

  return (
    <div className="flex flex-col">
      <DetailsHeader songData={song} />
      <div className="mb-10">
        <h2 className="text-white text-3xl font-bold">Description</h2>
        <div className="mt-5">
          <p className="text-gray-200 text-base my-1">
            {song.Description}
          </p>

          {/*{song.Description ? (<p>
            {song.Description}
          </p>) : (
            <p>Sorry, no description</p>
          )}*/}
        </div>
      </div>

      <div> <div className="flex flex-row justify-between">
        <h2 className="text-white text-3xl font-bold">Add to playlist</h2>
        <div className="flex flex-row gap-x-6 justify-between">
          <div className="col-span-3">
            {/* ... (existing code) */}
            <div className="mt-2 flex gap-x-4">
              {playlists && (
                  <select
                      onChange={(e) => setPlaylistId(e.target.value)}
                      value={playlistId}
                      className="min-w-[150px] bg-[#520038] text-gray-300 p-2 text-base rounded-lg outline-none sm:mt-0 mt-5 focus:ring-0 border-transparent focus:border-transparent"
                  >
                    {playlists.map((playlist) => (
                        <option key={playlist.PlaylistID} value={playlist.PlaylistID}>
                          {playlist.Name}
                        </option>
                    ))}
                  </select>
              )}

              <button
                  type="button"
                  className="min-w-[60px] rounded-md bg-cyan-500 px-3 py-2 text-sm text-white shadow-sm"
                  onClick={handleSubmitForm}
              >
                Save
              </button>
            </div>
          </div>
        </div>
      </div>


        <div className="mt-6 flex flex-wrap sm:justify-start justify-center gap-8">
          {playlists?.map((playlist, i) => (
              <PlaylistCard
                  playlist={playlist}
                  disable={true}
              />
          ))}
        </div>
      </div>
    </div>
  );
};

export default SongDetails;



