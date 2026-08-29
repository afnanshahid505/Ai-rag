const API_URL=import.meta.env.API_URL;
export const getInterviewquestions = async()=>{
    const response= await fetch(`${API_URL}/interview/questions`);

if(!response.ok){
    throw new Error("Failed to fetch the questions");
    
}

return response.json();
};