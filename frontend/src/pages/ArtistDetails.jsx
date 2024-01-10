import { useParams } from "react-router-dom";
import { useSelector } from "react-redux";
import { DetailsHeader, Error, Loader, RelatedSongs } from "../components";

import { useGetArtistDetailsQuery } from "../redux/services/shazamCore";
import useGetArtist from "../hooks/artist/useGetArtist";
import useGetAllSongsByArtist from "../hooks/song/useGetAllSongsByArtist";
import ArtistDetailsHeader from "../components/ArtistDetailsHeader";
import {TopChartCard} from "../components/TopPlay";

const ArtistDetails = () => {
  const { id: artistId } = useParams();
  const { activeSong, isPlaying, genreListId } = useSelector(
      (state) => state.player
  );
  const {artist} = useGetArtist(artistId)


  const {songs, loading, error } = useGetAllSongsByArtist(artistId)


  if (loading) return <Loader title="Loading top artists" />;

  if (error) return <Error />;

  return (
    <div className="flex flex-col">
      <ArtistDetailsHeader artistId={artistId} artistData={artist} />

      <h1 className="font-bold text-3xl text-white">Author's songs</h1>
        <div className="mt-4 flex flex-col gap-1">

            {songs?.map((song, i) => (
                <TopChartCard
                    key={song.SongID}
                    song={song}
                    i={i}
                    isPlaying={isPlaying}
                    activeSong={activeSong}
                    data={songs}
                />
            ))}
        </div>
    </div>
  );
};

export default ArtistDetails;
