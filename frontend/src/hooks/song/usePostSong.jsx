import {useEffect, useState} from "react";

const useGetSong = ({song}) => {

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        const addSongs = async () => {
            try{
                setLoading(true);

                const response = await fetch(`http://127.0.0.1:5000/songs/`,{
                    method: 'POST',
                    headers:
                        {
                            "Content-type": "application/json",
                        },
                    body: JSON.stringify(song)
                });

                if (!response.ok){
                    throw new Error('Failed to add a new song');
                }

            }catch (e){
                setError(e);
            }finally {
                setLoading(false)
            }
        };

        if(song){
            addSongs();
        }


    }, [song]);
    return {loading, error};
}

export default useGetSong;