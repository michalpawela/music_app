import {useEffect, useState} from "react";
import axios from "axios";
import {Error} from "../../components";

const useGetAllPlaylists = () => {
    const [playlists, setPlaylists] = useState();
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchPlaylists = async () => {
            try{
                const response = await axios.get('http://127.0.0.1:5000/playlists/', {
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }
                });


                if (response.status !== 200) {
                    throw new Error('Failed to fetch artist');
                }

                const data =  response.data;
                setPlaylists(data.playlists);
            }catch (e){
                setError(e);
            }finally {
                setLoading(false)
            }
        };

        fetchPlaylists();

    }, []);
    return {playlists, loading, error};
}

export default useGetAllPlaylists;