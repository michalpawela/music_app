import { Link } from "react-router-dom";

const ArtistDetailsHeader = ({ artistData }) => {
    const data = artistData.artist;

    console.log(data)
    return (
        <div className="relative w-full flex flex-col">
            <div className="w-full bg-gradient-to-l from-transparent to-black sm:h-48 h-28" />
            <div className="absolute inset-0 flex items-center">
                <img
                    alt="art"
                    className="sm:w-48 w-28 sm:h-48 h-28 rounded-full object-cover border-2 shadow-xl shadow-black"
                    src={`data:image/jpeg;base64, ${data.Photo}`}
                />

                <div className="ml-5">
                    <p className="font-bold sm:text-3xl text-xl text-white">
                        {data.Full_Name}
                    </p>
                </div>
            </div>

            <div className="w-full sm:h-44 h-24 " />
        </div>
    );
};

export default ArtistDetailsHeader;
