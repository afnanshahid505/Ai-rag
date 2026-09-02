const API_URL=import.meta.env.VITE_API_URL;
export const getInterviewquestions = async()=>{
    const response= await fetch(`${API_URL}/interview/questions`);

if(!response.ok){
    throw new Error("Failed to fetch the questions");
    
}

return response.json();
};

export const UploadResume = async(file)=>{
    const formData=new FormData();
    formData.append("file",file);
    const response= await fetch(`${API_URL}/interview/upload-resume`,{
        method:"POST",
        body:formData
    });
    if(!response.ok){
        throw new Error("Failed to upload the resume");
    }
    return response.json();
};