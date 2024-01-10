import SongBar from "./SongBar";

const RelatedSongs = ({song, isPlaying, activeSong, data, i,
  artistId,
}) => {

    return (
        <div className="flex flex-col">
            <h1 className="font-bold text-3xl text-white">Author's songs</h1>

            <div className="mt-6 w-full flex flex-col">
                {data?.map((song, i) => (
                    <SongBar
                        key={song.Title}
                        song={song}
                        i={i}
                        artistId={artistId}
                        isPlaying={isPlaying}
                        activeSong={activeSong}
                        handlePauseClick={handlePauseClick}
                        handlePlayClick={handlePlayClick}
                    />
                ))}
            </div>
        </div>
    );
}

export default RelatedSongs;
