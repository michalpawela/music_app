import React from 'react';
import {useParams} from "react-router-dom";
import useGetPlaylist from "../hooks/playlist/useGetPlaylist";
import {Error, Loader} from "../components";
import SongCardAPI from "../components/SongCardAPI";
import {useSelector} from "react-redux";
import SongPlaylistCard from "../components/SongPlaylistCard";
import {playPause, setActiveSong} from "../redux/features/playerSlice";

const PlaylistDetails = () => {
    const { playlistid } = useParams();
    const { activeSong, isPlaying, genreListId } = useSelector(
        (state) => state.player
    );
    const {playlist, loading, error} = useGetPlaylist(playlistid)


    if (loading) return <Loader title="Loading top artists" />;

    if (error) return <Error />;

    console.log(playlist.Songs[0])
    return (
        <div className="flex flex-col">
            <h2 className="font-bold text-3xl text-white text-left mt-4 mb-10">
                Playlist {playlist.Name}
            </h2>

            <div className="flex flex-wrap sm:justify-start justify-center gap-8">
                {playlist.Songs?.map((song, i) => (
                    <SongPlaylistCard
                        key={song.SongID}
                        song1={song}
                        songId={song.SongID}
                        isPlaying={isPlaying}
                        activeSong={activeSong}
                        data={playlist.Songs}
                        i={i}
                    />
                ))}
            </div>
        </div>
    );
};

export default PlaylistDetails;
