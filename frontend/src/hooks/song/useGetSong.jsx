import {useEffect, useState} from "react";

const useGetSong = (id) => {
    const [song, setSong] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchSongs = async () => {
            try{
                const response = await fetch(`http://127.0.0.1:5000/songs/${id}`,{
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
                setSong(data);
            }catch (e){
                setError(e);
            }finally {
                setLoading(false)
            }
        };

        fetchSongs();

    }, []);
    return {song, loading, error};
}

export default useGetSong;