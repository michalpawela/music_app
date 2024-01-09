import {useEffect, useState} from "react";
import axios from "axios";

const useAddSong = ({playlist}) => {

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    console.log(song)

    useEffect(() => {
        const addPlaylistSong = async () => {
            try{
                const response = await axios.post('http://127.0.0.1:5000/playlists/', playlist, {
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }
                });

                if (!response.data || response.status !== 201) {
                    throw new Error('Failed to add a new playlist song');
                }

            } catch (e) {
                console.error(e);
            } finally {
                console.log('Finally block');
            }}

        if(song){
            addPlaylistSong();
        }


    }, [song]);
    return {loading, error};
}

export default useAddSong;