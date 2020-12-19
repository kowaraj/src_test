import {
  RecoilRoot,
} from 'recoil';

import MyTodoList from './TodoList';

function MyApp() {
    return (
      <RecoilRoot>
        <MyTodoList />
      </RecoilRoot>
    );
  }

export default MyApp;