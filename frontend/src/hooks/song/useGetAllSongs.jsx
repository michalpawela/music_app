import {useEffect, useState} from "react";

const useGetAllSongs = () => {
    const [songs, setSongs] = useState([]);

    useEffect(() => {
        fetch('')
            .then((res) => res.json())
            .then((data) => setSongs(data));
    }, []);
}

export default useGetAllSongs;