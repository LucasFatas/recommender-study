const inputStyle = "appearance-none rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer";

export const RadioButton = (props) => {

  const {
    answers, 
    value, 
    questionNumber, 
    onChange,
    type
  } = props;

  return (
    <input 
      type="radio" 
      className={inputStyle} 
      value={value}
      name={`${questionNumber}${type}`}
      onChange={e => onChange(e, questionNumber)}
      defaultChecked={answers.get(questionNumber + 1) === value}
    /> 
  )
}