import { useSelector } from "react-redux";

import { Error, Loader, SongCard } from "../components";
import { useGetTopChartsQuery } from "../redux/services/shazamCore";
import useGetAllSongs from "../hooks/song/useGetAllSongs";
import SongCardAPI from "../components/SongCardAPI";

const TopCharts = () => {

  const { activeSong, isPlaying } = useSelector((state) => state.player);
  const {songs, loading, error} = useGetAllSongs()
  if (loading) return <Loader title="Loading Top charts" />;
    console.log(activeSong)
  if (error) return <Error />;

  return (
    <div className="flex flex-col">
      <h2 className="font-bold text-3xl text-white text-left mt-4 mb-10">
        Top Charts
      </h2>

      <div className="flex flex-wrap sm:justify-start justify-center gap-8">
        {songs?.map((song, i) => (
          <SongCardAPI
            key={song.SongID}
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

export default TopCharts;
