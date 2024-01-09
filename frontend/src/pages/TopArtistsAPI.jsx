import { useNavigate } from "react-router-dom";

const ArtistCardAPI = ({ artist }) => {
    const navigate = useNavigate();

    return (
        <div
            className="flex flex-col w-[250px] p-4 bg-white/5 bg-opacity-80 backdrop-blur-sm
            animate-slideup rounded-lg cursor-pointer"
            onClick={() => navigate(`/artists/${artist.ArtistID}`)}
        >
            <img
                alt="artists"
                src={`data:image/jpeg;base64, ${artist.Photo}`}
                className="w-full h-56 rounded-lg object-cover"
            />
            <p className="mt-4 font-semibold text-lg text-white truncate">
                {artist?.Full_Name}
            </p>
        </div>
    );
};

export default ArtistCardAPI;
