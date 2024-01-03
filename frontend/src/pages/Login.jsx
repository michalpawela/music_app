import React, {useState} from 'react';
import logo from '../assets/favicon.ico'
import {useDispatch, useSelector} from "react-redux";
import {loginUser} from "../redux/features/userSlice";
import {useNavigate} from "react-router-dom";
const Login = () => {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const {loading, error} = useSelector((state) => state.user);
    const handleLogin = (e) => {
        e.preventDefault();
        let userCredentials = {
            email,
            password
        }
        dispatch(loginUser(userCredentials)).then((result) => {
            if(result.payload){
                setEmail('');
                setPassword('');
                navigate('/')
            }
        });
    }

    return (
        <div className="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
            <div className="py-12">
                <div className="sm:mx-auto sm:w-full sm:max-w-sm">
                    <img
                        className="mx-auto h-10 w-auto"
                        src={logo}
                        alt="Music app"
                    />
                    <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-white">
                        Sign in to your account
                    </h2>
                </div>

                <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
                    <form action="" className="space-y-6" onSubmit={handleLogin}>
                        <div>
                            <label className="block text-sm font-medium leading-6 text-white">
                                Email
                            </label>

                            <div className="mt-2">
                                <input id="email"
                                       name="email"
                                       type="email"
                                       autoComplete="email"
                                       required
                                       value={email}
                                       onChange={(e) => setEmail(e.target.value)}
                                       className="block w-full rounded-md border-0 bg-white/70 py-1.5 text-black shadow-sm focus:ring-0"/>
                            </div>
                        </div>

                        <div>
                            <label className="block text-sm font-medium leading-6 text-white">
                                Password
                            </label>

                            <div className="mt-2">
                                <input id="password"
                                       name="password"
                                       type="password"
                                       autoComplete="password"
                                       required
                                       value={password}
                                       onChange={(e) => setPassword(e.target.value)}
                                       className="block w-full rounded-md border-0 bg-white/70 py-1.5 text-black shadow-sm focus:ring-0"/>
                            </div>
                        </div>

                        <div>
                            <button type="submit" className="flex w-full justify-center rounded-md bg-white px-3 py-1.5 text-sm font-semibold text-black shadow-sm">
                                {loading ? 'Loading...' : 'Sign In'}
                            </button>
                            {
                                error && (
                                    <div>
                                        {error}
                                    </div>
                                )
                            }
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default Login;
