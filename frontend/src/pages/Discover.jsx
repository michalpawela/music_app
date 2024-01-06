import { useDispatch, useSelector } from "react-redux";
import { Error, Loader, SongCard } from "../components";
import { genres } from "../assets/constants";
import {
  useGetSongsByGenreQuery,
  useGetTopChartsQuery,
} from "../redux/services/shazamCore";
import { selectGenreListId } from "../redux/features/playerSlice";
import useGetAllGenres from "../hooks/genre/useGetAllGenres";

const Discover = () => {
  const dispatch = useDispatch();
  const { activeSong, isPlaying, genreListId } = useSelector(
    (state) => state.player
  );
  const { data, isFetching } = useGetSongsByGenreQuery(
    genreListId || "POP"
  );
  const genreTitle = genres.find(({ value }) => value === genreListId)?.title;

  const {genresV2, loading,error} = useGetAllGenres();


  if (loading) return <Loader title="Loading songs..." />;

  if (error) return <Error />;

  return (
    <div className="flex flex-col">
      <div className="w-full flex justify-between items-center sm:flex-row flex-col mt-4 mb-10">
        <h2 className="font-bold text-3xl text-white text-left">
          Discover {genreTitle}
        </h2>
        <select
          onChange={(e) => dispatch(selectGenreListId(e.target.value))}
          value={genreListId || "pop"}
          className="min-w-[150px] bg-[#520038] text-gray-300 p-3 text-base rounded-lg outline-none sm:mt-0 mt-5 focus:ring-0 border-transparent focus:border-transparent"
        >
          {genres.map((genre) => (
            <option key={genre.value} value={genre.value}>
              {genre.title}
            </option>
          ))}
        </select>
      </div>

      <div className="flex flex-wrap sm:justify-start justify-center gap-8">
        {data?.map((song, i) => (
          <SongCard
            key={song.key}
            song={song}
            isPlaying={isPlaying}
            activeSong={activeSong}
            data={data}
            i={i}
          />
        ))}
      </div>
    </div>
  );
};

export default Discover;
