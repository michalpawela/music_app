import React, {useState} from 'react';
import { PhotoIcon, UserCircleIcon } from '@heroicons/react/24/solid'

const AddSong = () => {
    const [file, setFile] = useState(null);
    const handleFileChange = (event) => {
        const file = event.target.files[0];
        setFile(file);
        console.log(file.type)
    };

    return (
        <div className="mt-10">
            <form>
                <div className="space-y-12">
                    <div className="border-b border-white/10 pb-12">
                        <h2 className="text-base font-semibold leading-7 text-white">
                            Song information
                        </h2>

                        <p className="mt-1 text-sm leading-6 text-gray-300">
                            This information will be displayed for other users.
                        </p>

                        <div className="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                            <div className="sm:col-span-4">
                                <label htmlFor="song-title" className="block text-sm font-medium leading-6 text-white">
                                    Song title
                                </label>

                                <div className="mt-2">
                                    <div className="flex rounded-md bg-white/5 ring-1 ring-inset ring-white/10 ">
                                        <input type="text"
                                               name="song-title"
                                               id="song-title"
                                               className="flex-1 border-0 bg-transparent py-1.5 pl-1 text-white focus:ring-0 sm:text-sm"
                                        placeholder="Song title"/>
                                    </div>
                                </div>
                            </div>

                            <div className="sm:col-span-3">
                                <label htmlFor="category" className="block text-sm font-medium leading-6 text-white">
                                    Category
                                </label>
                                <div className="mt-2">
                                    <select
                                        id="category"
                                        name="category"
                                        className="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-0 sm:text-sm sm:leading-6 [&_*]:text-black"
                                    >
                                        <option>Pop</option>
                                        <option>Rap</option>
                                        <option>Country</option>
                                    </select>
                                </div>
                            </div>

                            <div className="col-span-full">
                                <label htmlFor="description" className="block text-sm font-medium leading-6 text-white">
                                    Song description
                                </label>
                                <div className="mt-2">
                                    <textarea
                                    id="description"
                                    name="description"
                                    rows={5}
                                    defaultValue={''}
                                    className="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-0"/>
                                </div>
                                <p className="mt-3 text-sm leading-6 text-gray-400">Write a few sentences about your song.</p>
                            </div>

                            <div className="col-span-full">
                                <label htmlFor="cover-photo" className="block text-sm font-medium leading-6 text-white">
                                    Cover photo
                                </label>
                                <div className="mt-2 flex justify-center rounded-lg border border-dashed border-white/25 px-6 py-10">
                                    <div className="text-center">
                                        <PhotoIcon className="mx-auto h-12 w-12 text-gray-500" aria-hidden="true" />
                                        <div className="mt-4 flex text-sm leading-6 text-gray-400">
                                            <label
                                                htmlFor="file-upload"
                                                className="relative cursor-pointer rounded-md bg-gray-900 font-semibold text-white"
                                            >
                                                <span className="p-3 focus:ring-0">Upload a file</span>
                                                <input id="file-upload" name="file-upload" type="file" accept="audio/mp3"
                                                       onChange={handleFileChange} className="sr-only"  />
                                            </label>
                                            <p className="pl-1">or drag and drop</p>
                                        </div>
                                        <p className="text-xs leading-5 text-gray-400">PNG, JPG, GIF up to 10MB</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="mt-6 flex items-center justify-end gap-x-6">
                    <button type="button" className="text-sm font-semibold leading-6 text-white">Cancel</button>
                    <button type="submit" className="rounded-md bg-cyan-500 px-3 py-2 text-sm text-white shadow-sm">Save</button>
                </div>
            </form>
        </div>
    );
};

export default AddSong;
