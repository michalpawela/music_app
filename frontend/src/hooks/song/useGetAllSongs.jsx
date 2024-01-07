import {useEffect, useState} from "react";
import axios from "axios";
import {Error} from "../../components";

const useGetAllSongs = () => {
    const [songs, setSongs] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchSongs = async () => {
            try{
                const response = await axios.get('http://127.0.0.1:5000/songs/', {
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }
                });


                if (response.status !== 200) {
                    throw new Error('Failed to fetch artist');
                }

                const data =  response.data;
                setSongs(data.songs);
            }catch (e){
                setError(e);
            }finally {
                setLoading(false)
            }
        };

        fetchSongs();

    }, []);
    return {songs, loading, error};
}

export default useGetAllSongs;