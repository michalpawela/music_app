import {useEffect, useState} from "react";
import axios from "axios";

const useGetGenre = (id) => {
    const [genre, setGenre] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchGenre = async () => {
            try{
                const response = await axios.get(`http://127.0.0.1:5000/genres/${id}`,{
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }
                });

                if (response.status !== 200){
                    throw new Error('Failed to fetch genres');
                }

                const data = response.data;
                console.log(data)
                setGenre(data.genre);
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