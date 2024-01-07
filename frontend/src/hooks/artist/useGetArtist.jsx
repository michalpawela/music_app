import {useEffect, useState} from "react";
import axios from "axios";
import {Error} from "../../components";

const useGetArtist = (id) => {
    const [artist, setArtist] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchArtist = async () => {
            try{
                const response =  await axios.get(`http://127.0.0.1:5000/artists/${id}`,{
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }
                });

                if (response.status !== 200) {
                    throw new Error('Failed to fetch artist');
                }

                const data =  response.data;
                setArtist(data);
            }catch (e){
                setError(e);
            }finally {
                setLoading(false)
            }
        };

        fetchArtist();

    }, []);
    return {artist, loading, error};
}

export default useGetArtist;