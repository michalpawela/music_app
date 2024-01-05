import {useEffect, useState} from "react";

const useGetArtist = (id) => {
    const [artist, setArtist] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchArtist = async () => {
            try{
                const response = await fetch(`http://127.0.0.1:5000/artists/${id}`,{
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