import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";
import PlayPause from "./PlayPause";
import { playPause, setActiveSong } from "../redux/features/playerSlice";
import useGetUser from "../hooks/user/useGetUser";
import {Error, Loader} from "./index";
import React, {useState} from "react";
import useGetAllPlaylist from "../hooks/playlist/useGetAllPlaylist";

const PlaylistCard = ({disable, playlist}) => {
    const dispatch = useDispatch();

    const {user, loading, error} = useGetUser(playlist.UserID)
    if (loading) return <Loader title="Loading songs..." />;

    if (error) return <Error />;

    return (
        <div className="flex flex-col w-[250px] p-4 bg-white/5 bg-opacity-80 backdrop-blur-sm animate-slideup rounded-lg cursor-pointer">
            <div className="relative w-full h-56 group">

                {disable ? (
                    <div
                        className={`absolute inset-0 justify-center items-center bg-black bg-opacity-50 flex`}
                    >
                        <div className="mt-4 flex flex-col items-center">
                            <p className="font-semibold text-lg text-white truncate items-center">
                                {playlist.Name}
                            </p>
                            <p className="text-sm truncate text-gray-300 mt-1 ">
                                {user.Name} {user.Surname}
                            </p>
                            <p className="text-sm truncate text-gray-300 mt-1">
                                {user.Username}
                            </p>
                        </div>
                    </div>
                ) : (
                    <Link to={`/playlists/${playlist.PlaylistID}`}>
                        <div
                            className={`absolute inset-0 justify-center items-center bg-black bg-opacity-50 flex`}
                        >
                            <div className="mt-4 flex flex-col items-center">
                                <p className="font-semibold text-lg text-white truncate items-center">
                                    {playlist.Name}
                                </p>
                                <p className="text-sm truncate text-gray-300 mt-1 ">
                                    {user.Name} {user.Surname}
                                </p>
                                <p className="text-sm truncate text-gray-300 mt-1">
                                    {user.Username}
                                </p>
                            </div>
                        </div>
                    </Link>
                )}
            </div>
        </div>
    );
};

export default PlaylistCard;
