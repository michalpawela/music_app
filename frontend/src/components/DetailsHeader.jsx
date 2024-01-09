import { Link } from "react-router-dom";

const DetailsHeader = ({ songData, artistData }) => {
  const artist = songData?.Artist;
    console.log(artistData)

  return (
    <div className="relative w-full flex flex-col">
      <div className="w-full bg-gradient-to-l from-transparent to-black sm:h-48 h-28" />
      <div className="absolute inset-0 flex items-center">
        <img
          alt="art"
          className="sm:w-48 w-28 sm:h-48 h-28 rounded-full object-cover border-2 shadow-xl shadow-black"
          src={`data:image/jpeg;base64, ${artist.Photo || (artistData && artistData.Album.Cover)}`}
        />

        <div className="ml-5 flex flex-col gap-4">
            <p className="font-bold sm:text-3xl text-xl text-white">
                {songData.Title}
            </p>
            <div>
                <p className="font-semibold sm:text-smtext-sm text-white">
                    {artist.Full_Name}
                </p>
                <p className="font-semibold sm:text-smtext-sm text-gray-400">
                    {songData.Album.Title}
                </p>
            </div>

          {/*{!artistId && (
            <Link to={`/artists/${songData?.artists[0].adamid}`}>
              <p className="text-base text-gray-400 mt-2">
                {songData?.subtitle}
              </p>
            </Link>
          )}*/}

          {/*<p className="text-base text-gray-400 mt-1">
            {artistId ? artist?.genreNames[0] : songData?.genres?.primary}
          </p>*/}
        </div>
      </div>

      <div className="w-full sm:h-44 h-24 " />
    </div>
  );
};

export default DetailsHeader;
