import { useDispatch, useSelector } from "react-redux";
import { Error, Loader, SongCard } from "../components";
import { genres } from "../assets/constants";
import {
  useGetSongsByGenreQuery,
  useGetTopChartsQuery,
} from "../redux/services/shazamCore";
import {playPause, selectGenreListId} from "../redux/features/playerSlice";
import useGetAllGenres from "../hooks/genre/useGetAllGenres";
import useGetAllSongs from "../hooks/song/useGetAllSongs";
import {useEffect, useRef, useState} from "react";
import axios from "axios";
import {Song} from "../models/models";
import useGetArtist from "../hooks/artist/useGetArtist";
import useGetAllSongsByArtist from "../hooks/song/useGetAllSongsByArtist";
import SongCardAPI from "../components/SongCardAPI";
import useGetGenre from "../hooks/genre/useGetGenre";

const Discover = () => {
  const dispatch = useDispatch();
  const { activeSong, isPlaying, genreListId } = useSelector(
    (state) => state.player
  );

  const [genreId, setGenreId] = useState(1)

  const {songs, loading, error} = useGetAllSongsByArtist(genreId)

  const{genresV2} = useGetAllGenres()

  const {genre} = useGetGenre(genreId)


  if (loading) return <Loader title="Loading songs..." />;

  if (error) return <Error />;

  return (

    <div className="flex flex-col">
      <div className="w-full flex justify-between items-center sm:flex-row flex-col mt-4 mb-10">
        <h2 className="font-bold text-3xl text-white text-left">
          Discover <span key={genreId}>{genre.Name}</span>
        </h2>

        <select
          onChange={(e) => setGenreId(e.target.value)}
          value={genreId}
          className="min-w-[150px] bg-[#520038] text-gray-300 p-3 text-base rounded-lg outline-none sm:mt-0 mt-5 focus:ring-0 border-transparent focus:border-transparent"
        >
          {genresV2.map((genre) => (
            <option key={genre.GenreID} value={genre.GenreID}>
              {genre.Name}
            </option>
          ))}
        </select>
      </div>

      <div className="flex flex-wrap sm:justify-start justify-center gap-8">
        {songs?.map((song, i) => (
          <SongCardAPI
            key={song.key}
            song={song}
            isPlaying={isPlaying}
            activeSong={activeSong}
            data={songs}
            i={i}
          />
        ))}
      </div>


    </div>
  );
};

export default Discover;
