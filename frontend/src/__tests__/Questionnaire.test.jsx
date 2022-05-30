
import renderer from "react-test-renderer";
import { ConsentPage } from "../components/pages/ConsentPage";

it("Questionnaire test", () => {
  const component = renderer.create(
    <ConsentPage defaultPage="/default"/>
  );

  let tree = component.toJSON();
  expect(tree).toMatchSnapshot();

  // manually trigger the callback
  renderer.act(() => {
    tree.props.onMouseEnter();
  });
  // re-rendering
  tree = component.toJSON();
  expect(tree).toMatchSnapshot();

  // manually trigger the callback
  renderer.act(() => {
    tree.props.onMouseLeave();
  });
  // re-rendering
  tree = component.toJSON();
  expect(tree).toMatchSnapshot();
})