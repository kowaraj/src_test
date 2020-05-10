// import { Select } from 'antd';
module Select = {
    [@bs.module "antd"]
    [@react.component]
    external make : unit => React.element = "Select";
};
