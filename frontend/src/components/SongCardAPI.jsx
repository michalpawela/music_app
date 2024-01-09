import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";
import PlayPause from "./PlayPause";
import { playPause, setActiveSong } from "../redux/features/playerSlice";

const SongCardAPI = ({ song, isPlaying, activeSong, data, i }) => {
  const dispatch = useDispatch();

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

          <img alt="song_img" src={`data:image/jpeg;base64, ${song.Album.Cover}`} />
        </div>
        <div className="mt-4 flex flex-col">
          <p className="font-semibold text-lg text-white truncate">
            <Link to={`/songs/${song?.SongID}`}>{song.Title}</Link>
          </p>
          <p className="text-sm truncate text-gray-300 mt-1">
            {song.Description}
            <Link
                to={
                   `/artists/${song?.Artist.ArtistId}`

                }
            >
            </Link>
          </p>
        </div>
      </div>
  );
};

export default SongCardAPI;
