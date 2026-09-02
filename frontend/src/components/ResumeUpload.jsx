import {useState} from "react";
import {UploadResume} from "../services/interviewApi";
function ResumeUpload(){
    const [file,setFile]=useState(null);
    const [loading,setLoading]=useState(false);
    const[message,setMessage]=useState("");
    const handleSubmit=(e)=>{
        e.preventDefault();
        if(!file){
            setMessage("Please select a file to upload");
            return;
        }
        try{
            setLoading(true);
            setMessage("Uploading resume...");
            const data=await UploadResume(file);
            setMessage(`Resume uploaded successfully: ${data.fileName}`);
            setFile(null);
        }catch(error){
            setMessage(`Error: ${error.message}`);
        }finally{
            setLoading(false);
        }
    }

return(
    <div>
        <h2>Upload Resume</h2>
        <form onSubmit={handleSubmit}>
            <input type="file" accept=".pdf" onChange={(e)=>setFile(e.target.files[0])} />
            <button type="submit" disabled={loading}>{loading?"Uploading...":"Upload"}</button>
        </form>
        {message && <p>{message}</p>}
    </div>
);
}
export default ResumeUpload;