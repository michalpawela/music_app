import {useEffect, useState} from "react";

const useGetAllSongs = () => {
    const [songs, setSongs] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchSongs = async () => {
            try{
                const response = await fetch('http://127.0.0.1:5000/songs/',{
                    method: 'GET',
                    headers:
                        {
                            "Content-type": "application/json",
                        },
                });

                if (!response.ok){
                    throw new Error('Failed to fetch genres');
                }

                const data = await response.json();
                setSongs(data);
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