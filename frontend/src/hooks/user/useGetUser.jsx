import {useEffect, useState} from "react";
import axios from "axios";
import {Error} from "../../components";

const useGetUser = (id) => {
    const [user, setUser] = useState();
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchUser = async () => {
            try{
                const response = await axios.get(`http://127.0.0.1:5000/users/${id}`,{
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }
                });

                if (response.status !== 200) {
                    throw new Error('Failed to fetch artist');
                }

                const data = response.data;
                console.log(data)
                setUser(data.user);
            }catch (e){
                setError(e);
            }finally {
                setLoading(false)
            }
        };

        fetchUser();

    }, []);
    return {user, loading, error};
}

export default useGetUser;