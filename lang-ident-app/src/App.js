import './App.css';

function MyButton() {
  return (
    <button>
      record (this does nothing)
    </button>
  );
}

export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}