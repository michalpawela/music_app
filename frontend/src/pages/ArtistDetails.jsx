import { useParams } from "react-router-dom";
import { useSelector } from "react-redux";
import { DetailsHeader, Error, Loader, RelatedSongs } from "../components";

import { useGetArtistDetailsQuery } from "../redux/services/shazamCore";
import useGetArtist from "../hooks/artist/useGetArtist";
import useGetAllSongsByArtist from "../hooks/song/useGetAllSongsByArtist";
import ArtistDetailsHeader from "../components/ArtistDetailsHeader";

const ArtistDetails = () => {
  const { id: artistId } = useParams();
  const { activeSong, isPlaying, genreListId } = useSelector(
      (state) => state.player
  );
  const {artist} = useGetArtist(artistId)


  const {songs, loading, error } = useGetAllSongsByArtist(artistId)


  if (loading) return <Loader title="Loading top artists" />;

  if (error) return <Error />;
  console.log(songs)
  return (
    <div className="flex flex-col">
      <ArtistDetailsHeader artistId={artistId} artistData={artist} />

      <RelatedSongs
        data={songs}
        artistId={artistId}
        isPlaying={isPlaying}
        activeSong={activeSong}
      />
    </div>
  );
};

export default ArtistDetails;
