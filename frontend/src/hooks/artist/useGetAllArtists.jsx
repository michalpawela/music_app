import {useEffect, useState} from "react";
import axios from "axios";
import {Error} from "../../components";

const useGetAllArtists = () => {
    const [artists, setArtists] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchArtists = async () => {
            try{
                const response = await axios.get('http://127.0.0.1:5000/artists/',{
                    headers:
                        {
                            "Content-type": "application/json",
                        },
                });

                if (response.status !== 200) {
                    throw new Error('Failed to fetch artist');
                }

                const data =  response.data;
                setArtists(data.artists);
            }catch (e){
                setError(e);
            }finally {
                setLoading(false)
            }
        };

        fetchArtists();

    }, []);
    return {artists, loading, error};
}

export default useGetAllArtists;