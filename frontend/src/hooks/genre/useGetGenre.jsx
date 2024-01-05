import {useEffect, useState} from "react";

const useGetGenre = (id) => {
    const [genre, setGenre] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchGenre = async () => {
            try{
                const response = await fetch(`http://127.0.0.1:5000/genres/${id}`,{
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
                setGenre(data);
            }catch (e){
                setError(e);
            }finally {
                setLoading(false)
            }
        };

        fetchGenre();

    }, []);
    return {genre, loading, error};
}

export default useGetGenre;