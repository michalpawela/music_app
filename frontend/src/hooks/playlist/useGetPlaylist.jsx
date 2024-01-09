import {useEffect, useState} from "react";
import axios from "axios";
import {Error} from "../../components";

const useGetPlaylist = (id) => {
    const [playlist, setSongs] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchPlaylist = async () => {
            try{
                const response = await axios.get(`http://127.0.0.1:5000/playlists/${id}`, {
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }
                });


                if (response.status !== 200) {
                    throw new Error('Failed to fetch playlist');
                }

                const data =  response.data;
                setSongs(data.playlist);
            }catch (e){
                setError(e);
            }finally {
                setLoading(false)
            }
        };

        fetchPlaylist();

    }, []);
    return {playlist, loading, error};
}

export default useGetPlaylist;