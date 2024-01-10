import {useEffect, useState} from "react";
import axios from "axios";
import {Error} from "../../components";

const useGetAllGenres = () => {
    const [genresV2, setGenresV2] = useState();
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchGenres = async () => {
            try{
                const response = await axios.get('http://127.0.0.1:5000/genres/',{
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }
                });

                if (response.status !== 200) {
                    throw new Error('Failed to fetch artist');
                }

                const data =  response.data;

                setGenresV2(data.genres);
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