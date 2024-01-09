import { useParams } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { DetailsHeader, Error, Loader, RelatedSongs } from "../components";

import { setActiveSong, playPause } from "../redux/features/playerSlice";
import {
  useGetSongDetailsQuery,
  useGetSongRelatedQuery,
} from "../redux/services/shazamCore";
import useGetSong from "../hooks/song/useGetSong";

const SongDetails = () => {
  const dispatch = useDispatch();
  const { songid } = useParams();
  const { activeSong, isPlaying } = useSelector((state) => state.player);
  const { song, loading, error } = useGetSong(songid)
  const handlePauseClick = () => {
    dispatch(playPause(false));
  };

  const handlePlayClick = () => {
    dispatch(playPause(true));
  };

  if (loading) {
    return <Loader title="Searching song details" />;
  }

  if (error) return <Error />;
console.log(song)
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

      {/*<RelatedSongs
        data={data}
        isPlaying={isPlaying}
        activeSong={activeSong}
        handlePauseClick={handlePauseClick}
        handlePlayClick={handlePlayClick}
      />*/}
    </div>
  );
};

export default SongDetails;


/*songData?.sections[1].type === "LYRICS" ? (
            songData?.sections[1].text.map((line, i) => (
              <p className="text-gray-200 text-base my-1">{line}</p>
            ))
          )*/