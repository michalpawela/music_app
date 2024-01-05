import {useEffect, useState} from "react";

const useGetAllGenres = () => {
    const [genresV2, setGenresV2] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchGenres = async () => {
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
                setGenresV2(data);
            }catch (e){
                setError(e);
            }finally {
                setLoading(false)
            }
        };

        fetchGenres();

    }, []);
    return {genresV2, loading, error};
}

export default useGetAllGenres;