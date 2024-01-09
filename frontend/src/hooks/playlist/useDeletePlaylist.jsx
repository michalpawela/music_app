import {useEffect, useState} from "react";
import axios from "axios";

const useAddSong = (id) => {

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);


    useEffect(() => {
        const deletePlaylist = async () => {
            try{
                const response = await axios.delete(`http://127.0.0.1:5000/playlists/${id}`,  {
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }
                });

                if (!response.data || response.status !== 201) {
                    throw new Error('Failed to delete playlist');
                }

            } catch (e) {
                console.error(e);
            } finally {
                console.log('Finally block');
            }}

        if(song){
            deletePlaylist();
        }


    }, [song]);
    return {loading, error};
}

export default useAddSong;