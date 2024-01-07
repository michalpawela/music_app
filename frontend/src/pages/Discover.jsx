import { useDispatch, useSelector } from "react-redux";
import { Error, Loader, SongCard } from "../components";
import { genres } from "../assets/constants";
import {
  useGetSongsByGenreQuery,
  useGetTopChartsQuery,
} from "../redux/services/shazamCore";
import {playPause, selectGenreListId} from "../redux/features/playerSlice";
import useGetAllGenres from "../hooks/genre/useGetAllGenres";
import useGetAllSongs from "../hooks/song/useGetAllSongs";
import {useEffect, useRef, useState} from "react";
import axios from "axios";
import {Song} from "../models/models";
import useGetArtist from "../hooks/artist/useGetArtist";

const Discover = () => {
  const dispatch = useDispatch();
  const { activeSong, isPlaying, genreListId } = useSelector(
    (state) => state.player
  );
  const { data, isFetching } = useGetSongsByGenreQuery(
    genreListId || "POP"
  );
  const genreTitle = genres.find(({ value }) => value === genreListId)?.title;



  const [songs, setSongs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchSongs = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/songs/', {
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
          }
        });

        if (response.status !== 200) {
          throw new Error('Failed to fetch songs');
        }

        const data = response.data;

        setSongs(data.songs);
      } catch (e) {
        setError(e);
        console.error(e);
      } finally {
        setLoading(false);
      }
    };

    fetchSongs();
  }, []);

  console.log(songs)

  const {artist} = useGetArtist(2);
  console.log(artist)


  if (loading) return <Loader title="Loading songs..." />;

  if (error) return <Error />;

  return (

    <div className="flex flex-col">
      <div className="w-full flex justify-between items-center sm:flex-row flex-col mt-4 mb-10">
        <h2 className="font-bold text-3xl text-white text-left">
          Discover {genreTitle}
        </h2>
        <select
          onChange={(e) => dispatch(selectGenreListId(e.target.value))}
          value={genreListId || "pop"}
          className="min-w-[150px] bg-[#520038] text-gray-300 p-3 text-base rounded-lg outline-none sm:mt-0 mt-5 focus:ring-0 border-transparent focus:border-transparent"
        >
          {genres.map((genre) => (
            <option key={genre.value} value={genre.value}>
              {genre.title}
            </option>
          ))}
        </select>
      </div>

      {/*<div>
        {songs?.map((song,i) => (
            <div key={i}>
              <p>{song.Title}</p>
              <AudioPlayer audioSrc={song.Song} />
            </div>
        ))}

      </div>*/}

      <div className="flex flex-wrap sm:justify-start justify-center gap-8">
        {data?.map((song, i) => (
          <SongCard
            key={song.key}
            song={song}
            isPlaying={isPlaying}
            activeSong={activeSong}
            data={data}
            i={i}
          />
        ))}
      </div>


    </div>
  );
};

export default Discover;
/*

const AudioPlayer = ({ audioSrc }) => {
  const { activeSong, currentSongs, currentIndex, isActive, isPlaying } = useSelector((state) => state.player);
  const [audio, setAudio] = useState(new Audio());
  const dispatch = useDispatch();
  const audioRef = useRef(new Audio());

  useEffect(() => {
    const audio = audioRef.current;

    if (audioSrc) {
      audio.src = `data:audio/mp3;base64,${audioSrc}`;
      audio.load();
    }

    return () => {
      // Cleanup when component is unmounted
      audio.pause();
      audio.src = '';
      audio.load();
    };
  }, [audioSrc]);

  useEffect(() => {
    const audio = audioRef.current;

    if (isPlaying) {
      audio.play().catch((error) => {
        console.error('Failed to play audio:', error);
        dispatch(playPause(false)); // Pause if there's an error playing the audio
      });
    } else {
      audio.pause();
    }
  }, [isPlaying]);

  const playPauseHandler = () => {
    dispatch(playPause(!isPlaying));
  };

  return (
      <div>
        <button onClick={playPauseHandler}>
          {isPlaying ? "Play" : "Pause"}
        </button>
      </div>
  );
};*/
