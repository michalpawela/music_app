import {useEffect, useState} from "react";
import axios from "axios";
import {Error} from "../../components";

const useGetAllAlbums = () => {
    const [albums, setAlbums] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchAlbums = async () => {
            try{
                const response = await axios.get('http://127.0.0.1:5000/albums/',{
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }
                });

                if (response.status !== 200) {
                    throw new Error('Failed to fetch artist');
                }

                const data =  response.data;
                setAlbums(data.albums);
            }catch (e){
                setError(e);

            }finally {
                setLoading(false)
            }
        };

        fetchAlbums();

    }, []);
    return {albums, loading, error};
}

export default useGetAllAlbums;