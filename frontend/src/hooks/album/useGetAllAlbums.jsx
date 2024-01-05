import {useEffect, useState} from "react";

const useGetAllAlbums = () => {
    const [albums, setAlbums] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchAlbums = async () => {
            try{
                const response = await fetch('http://127.0.0.1:5000/genres/',{
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
                setAlbums(data);
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