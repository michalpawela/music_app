import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";
import PlayPause from "./PlayPause";
import { playPause, setActiveSong } from "../redux/features/playerSlice";
import {useEffect, useState} from "react";

const SongCardAPI = ({ song, isPlaying, activeSong, data, i }) => {
  const dispatch = useDispatch();
  const [audio, setAudio] = useState(new Audio());

  useEffect(() => {
    if (song.Song) {
      audio.src = `data:audio/mp3;base64,${song.Song}`;
      audio.load();
    }

    return () => {
      // Cleanup when component is unmounted
      audio.pause();
      audio.src = "";
      audio.load();
    };
  }, [audio, song]);

  const handlePauseClick = () => {
    dispatch(playPause(false));
  };

  const handlePlayClick = () => {
    dispatch(setActiveSong({ song, data, i }));
    dispatch(playPause(true));
  };


  return (
    <div className="flex flex-col w-[250px] p-4 bg-white/5 bg-opacity-80 backdrop-blur-sm animate-slideup rounded-lg cursor-pointer">
      <div className="relative w-full h-56 group">
        <div
          className={`absolute inset-0 justify-center items-center bg-black bg-opacity-50 group-hover:flex ${
            activeSong?.Title === song.Title
              ? "flex bg-black bg-opacity-70"
              : "hidden"
          }`}
        >
          <PlayPause
            isPlaying={isPlaying}
            activeSong={activeSong}
            song={song}
            handlePause={handlePauseClick}
            handlePlay={handlePlayClick}
          />
        </div>
        <div className="w-48 h-48 bg-white text-black">
          song photo
          {/*<img alt="song_img" src={`data:image/jpeg;base64, ${song.Photo}`} />*/}
        </div>

      </div>
      <div className="mt-4 flex flex-col">
        <p className="font-semibold text-lg text-white truncate">
          <Link to={`/songs/${song?.key}`}>{song.title}</Link>
        </p>
        <p className="text-sm truncate text-gray-300 mt-1">
          {/*<Link
            to={
              song.artists
                ? `/artists/${song?.artists[0]?.adamid}`
                : "/top-artists"
            }

            {song.Description}
          </Link> >*/}
          {song.Description}
        </p>
      </div>
    </div>
  );
};

export default SongCardAPI;
