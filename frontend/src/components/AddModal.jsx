import {useState,Fragment} from "react";
import {Dialog, Transition} from "@headlessui/react";
import axios from "axios";
import {Error} from "./index";
import {useNavigate} from "react-router-dom";

const AddForm = ({isOpen, closeModal, userId}) =>{

    const [loading, setLoading] = useState(false);
    const [success, setSuccess] = useState(false)
    const [error, setError] = useState(false);
    const [submitting, setSubmitting] = useState(false);
    const [name, setName] = useState('');
    const navigate = useNavigate();

    const handleSubmitForm = async (event) => {
        event.preventDefault();

        const requestData = {
            Name: name,
            UserID: userId,
        };

        try{
            setLoading(true)
            const response = await axios.post('http://127.0.0.1:5000/playlists/', requestData, {
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                }
            });

            if (!response.data || response.status !== 201) {
                throw new Error('Failed to add a new song');
            }

            setSuccess(true);

            setTimeout(() => {
                setSuccess(false);
                closeModal();
                window.location.reload()

            }, 1000);




        } catch (e) {
            setError(true)
        } finally {
            setLoading(false)
        }

    }


    return(
        <>
            <Transition appear show={isOpen} as={Fragment}>
                <Dialog as="div" className="absolute z-30" onClose={closeModal}>
                    <Transition.Child
                        as={Fragment}
                        enter="ease-out duration-300"
                        enterFrom="opacity-0"
                        enterTo="opacity-100"
                        leave="ease-in duration-200"
                        leaveTo="opacity-0"
                        leaveFrom="opacity-100">
                        <div className="fixed inset-0 bg-gray-900 opacity-70"/>
                    </Transition.Child>

                    <div className="fixed inset-0 overflow-y-auto">
                        <div className="flex min-h-full items-center justify-center p-4 text-center ml-0 lg:ml-64">
                            <Transition.Child
                                as={Fragment}
                                enter="ease-out duration-300"
                                enterFrom="opacity-0 scale-95"
                                enterTo="opacity-100 scale-100"
                                leave="ease-in duration-200"
                                leaveTo="opacity-0 scale-95"
                                leaveFrom="opacity-100 scale-100">
                                <Dialog.Panel className="relative w-full max-w-lg overflow-y-auto transform rounded-xl bg-white  p-12 text-left  flex flex-col mt-12 shadow-gray-800 max-h-[90vh] tranition-all">
                                    <form onSubmit={handleSubmitForm} id="customer-add">
                                        <div className="space-y-12 sm:space-y-16">
                                            <div>
                                                <h2 className=" space-y-8 border-b  border-gray-200 py-3 sm:space-y-0 sm:divide-y  text-black divide-gray-200 ">Create Playlist </h2>


                                                <div className="mt-10 space-y-8 border-b border-gray-200 pb-12 sm:space-y-0 sm:divide-y sm:divide-gray-900/10 divide-gray-200 sm:border-t sm:pb-0">
                                                    <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                                                        <label className="block w-full bg-gray-200  rounded-md border-0 py-1.5  shadow-sm px-4 text-black focus:ring-1 focus:ring-inset focus:ring-gray-800 focus:ring-orange  sm:text-sm sm:leading-6">
                                                            Playlist Name
                                                        </label>
                                                        <div className="mt-2 sm:col-span-2 sm:mt-0">
                                                            <input

                                                                disabled={submitting}

                                                                type="text"
                                                                onChange={(e) => setName(e.target.value)}
                                                                required
                                                                className="block w-full bg-gray-200 rounded-md border-0 py-1.5 shadow-sm  focus:ring-1 focus:ring-inset focus:ring-gray-800 focus:ring-orange  sm:text-sm sm:leading-6"
                                                            />
                                                        </div>
                                                    </div>


                                                </div>
                                            </div>
                                        </div>

                                        <div className="mt-10 flex items-center justify-end gap-x-6">
                                            <button  className="border p-2 rounded-md">Cancel</button>
                                            <button type="submit" className="p-2 bg-cyan-400 rounded-md">Save</button>
                                        </div>
                                    </form>
                                </Dialog.Panel>
                            </Transition.Child>
                        </div>
                    </div>
                </Dialog>
            </Transition>
        </>
    )
}

export default AddForm;