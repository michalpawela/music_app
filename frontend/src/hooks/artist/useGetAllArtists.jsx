import {useEffect, useState} from "react";

const useGetAllArtists = () => {
    const [artists, setArtists] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchArtists = async () => {
            try{
                const response = await fetch('http://127.0.0.1:5000/artists/',{
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
                setArtists(data);
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