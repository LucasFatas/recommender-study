import loadingGif from '../../assets/loading.gif';

export const Loading = () => {
  
  return (
    <div className="w-screen h-screen flex justify-center items-center">
      <img src={loadingGif} alt="loading"/>
    </div>
  )
};
