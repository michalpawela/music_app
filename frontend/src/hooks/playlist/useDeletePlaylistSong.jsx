import {useEffect, useState} from "react";
import axios from "axios";

const useDeletePlaylistSong = ({song}) => {

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);


    useEffect(() => {
        const addSongs = async () => {
            try{
                const response = await axios.post('http://127.0.0.1:5000/playlists/remove_song', song, {
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }
                });

                if (!response.data || response.status !== 201) {
                    throw new Error('Failed to delete a song from playlist');
                }

            } catch (e) {
                console.error(e);
            } finally {
                console.log('Finally block');
            }}

        if(song){
            addSongs();
        }


    }, [song]);
    return {loading, error};
}

export default useDeletePlaylistSong;