import React, {useEffect, useState} from 'react';
import SongCardAPI from "../components/SongCardAPI";
import useGetAllPlaylists from "../hooks/playlist/useGetAllPlaylist";
import {Error, Loader} from "../components";
import PlaylistCard from "../components/PlaylistCard";
import AddForm from "../components/AddModal";

const Playlist = () => {
    const [openModal, setOpenModal] = useState(false)
    const {playlists, loading, error} = useGetAllPlaylists()

    if (loading) return <Loader title="Loading songs..." />;

    if (error) return <Error />;


    return (
        <div className="flex flex-col">
            <div className="w-full flex justify-between items-center sm:flex-row flex-col mt-4 mb-10">
                <h2 className="font-bold text-3xl text-white text-left">
                    User's playlist
                </h2>
                <button onClick={()=>setOpenModal(true)} className="p-3 rounded-md bg-cyan-400 font-semibold text-black">Create playlist</button>
            </div>

            <div className="flex flex-wrap sm:justify-start justify-center gap-8">
                {playlists?.map((playlist, i) => (
                    <PlaylistCard
                        playlist={playlist}
                    />
                ))}
            </div>
            <AddForm userId={playlists[0].UserID} isOpen={openModal} closeModal={()=> setOpenModal(false)}/>
        </div>
    );
};

export default Playlist;
