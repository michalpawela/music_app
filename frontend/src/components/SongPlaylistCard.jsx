import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";
import PlayPause from "./PlayPause";
import { playPause, setActiveSong } from "../redux/features/playerSlice";
import useGetSong from "../hooks/song/useGetSong";

const SongPlaylistCard = ({ song1,songId, isPlaying, activeSong, data, i }) => {
  const dispatch = useDispatch();

  const handlePauseClick = () => {
    dispatch(playPause(false));
  };
    const { song, loading, error } = useGetSong(songId);
  const handlePlayClick = () => {
    dispatch(setActiveSong({ song, data, i }));
    dispatch(playPause(true));
  };




  return (
      <div className="flex flex-col w-[250px] p-4 bg-white/5 bg-opacity-80 backdrop-blur-sm animate-slideup rounded-lg cursor-pointer">
        <div className="relative w-full h-56 group">
          <div
              className={`absolute inset-0 justify-center items-center bg-black bg-opacity-50 group-hover:flex ${
                  activeSong?.Title === song1.Title
                      ? "flex bg-black bg-opacity-70"
                      : "hidden"
              }`}
          >
            <PlayPause
                isPlaying={isPlaying}
                activeSong={activeSong}
                song={song1}
                handlePause={handlePauseClick}
                handlePlay={handlePlayClick}
            />
          </div>

          <img alt="song_img" src={`data:image/jpeg;base64, ${song?.Album.Cover}`} />
        </div>
        <div className="mt-4 flex flex-col">
          <p className="font-semibold text-lg text-white truncate">
            <Link to={`/songs/${song1?.SongID}`}>{song1.Title}</Link>
          </p>
          <p className="text-sm truncate text-gray-300 mt-1">
            {song1.Description}
          </p>
        </div>
      </div>
  );
};

export default SongPlaylistCard;
