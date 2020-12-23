import React from 'react';
import { RecoilRoot } from 'recoil';
import MyTodoList from './TodoList';

function App() {
  return (
      <RecoilRoot>
        <MyTodoList />
      </RecoilRoot>
  );
}

export default App;
