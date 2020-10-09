// import * as d3 from 'd3';
// import {roundTo20} from '../../utils/math';

// 結局foreign object一つにできるから、最終的にテキストで書いたhtmlを挿入できるという話 →kawano.js

function render(g, node, isSelected) {
  node.width = node.width || 400;
  node.height = node.height || 200;

  // ▼▼title background▼▼
  g.append("foreignObject")
    .attr("x", node.x)
    .attr("y", node.y)
    .attr("class", "title")
    .style("width", (node.width * 5) / 8 + "px")
    .style("height", node.height / 2 + "px")
    .append("xhtml:div")
    .style("width", (node.width * 5) / 8 + "px")
    .style("height", node.height / 2 + "px")
    // .style("background-color", "#3F3F3F")
    .style("background-color", "#FFFFFF")
    .style("border-radius", "8px 0 0 0")
    .style("box-sizing", "border-box")
    .style("border-top", "1px solid #707070")
    .style("border-left", "1px solid #707070")
    .style("border-bottom", "1px solid #707070")
    // .style("border-bottom", "1px solid #707070")

    // ▼▼title text▼▼
    // g.append('foreignObject')
    // .attr("x", node.x)
    // .attr("y", node.y)
    // .attr("class", "unselectable")
    // .style("width", node.width * 5 / 8 + "px")
    // .style("height", node.height / 2 + "px")
    // .style("display", "table")
    .append("xhtml:p")
    .style("display", "table-cell")
    .style("vertical-align", "middle")
    .style("width", (node.width * 5) / 8 + "px")
    .style("height", node.height / 2 + "px")
    .style("box-sizing", "border-box")
    .style("padding", "4px 8px 4px 8px")
    .style("color", "#525E6A")
    .style("font-weight", "bold")
    .style("font-size", "20px")
    .style("margin", 0)
    // .style("overflow-wrap", "break-word")
    // ▼▼▼▼以下、じん追記▼▼▼▼
    .style("display", "-webkit-box")
    .style("overflow", "hidden")
    .style("-webkit-line-clamp", "3")
    .style("-webkit-box-orient", "vertical")
    .style("line-height", "30px")
    // ▲▲▲▲以上（3行以降・・・になる）▲▲▲▲
    .text(() => node.title);

  // ▼▼thumbnail▼▼
  g.append("foreignObject")
    .attr("x", node.x + (node.width * 5) / 8)
    .attr("y", node.y)
    .style("width", (node.width * 3) / 8 + "px")
    .style("height", node.height / 2 + "px")
    .append("xhtml:div")
    .style("width", (node.width * 3) / 8 + "px")
    .style("height", node.height / 2 + "px")
    .style("background-image", `url(${node.thumbnail})`)
    .style("background-position", "center center")
    .style("background-size", "cover")
    .style("background-repeat", "no-repeat")
    .style("border-radius", "0 8px 0 0")
    .style("box-sizing", "border-box")
    // .style("border-top", "1px solid white")
    // .style("border-left", "1px solid white")
    .style("border", "1px solid #707070");

  // ▼▼summary background▼▼
  g.append("foreignObject")
    .attr("x", node.x)
    .attr("y", node.y + node.height / 2)
    .style("width", node.width + "px")
    .style("height", node.height / 2 + "px")
    .append("xhtml:div")
    .style("width", node.width + "px")
    .style("height", node.height / 2 + "px")
    // .style("background-color", "#707070")
    .style("background-color", "#FFFFFF")
    .style("box-sizing", "border-box")
    .style("border-radius", "0 0 8px 8px")
    .style("border-bottom", "1px solid #707070")
    .style("border-right", "1px solid #707070")
    .style("border-left", "1px solid #707070")

    // ▼▼summary text▼▼
    // g.append('foreignObject')
    //   .attr("x", node.x)
    //   .attr("y", node.y + node.height / 2)
    //   .attr("class", "unselectable")
    //   .style("width", node.width + "px")
    //   .style("height", node.height / 2 + "px")
    .append("xhtml:p")
    .style("width", node.width + "px")
    .style("height", node.height / 2 + "px")
    .style("box-sizing", "border-box")
    .style("padding", "8px 8px 8px 8px")
    .style("color", "#525E6A")
    .style("font-size", "16px")
    .style("margin", 0)
    // .style("overflow-wrap", "break-word")
    // ▼▼▼▼以下、じん追記▼▼▼▼
    .style("display", "-webkit-box")
    .style("overflow", "hidden")
    .style("-webkit-line-clamp", "4")
    .style("-webkit-box-orient", "vertical")
    .style("line-height", "22px")
    // ▲▲▲▲以上（4行以降・・・になる）▲▲▲▲
    .text(() => node.summary);

  // ここから元々あったrender
  // node.width = node.width || 120;
  // node.height = node.height || 60;
  // let borderColor = isSelected ? '#666666' : '#bbbbbb';
  // if (node.type !== 'start' && node.type !== 'end') {
  //   // title
  //   g.append('rect').
  //       attr('x', node.x).
  //       attr('y', node.y).
  //       attr('stroke', borderColor).
  //       attr('class', 'title').
  //       style('height', '20px').
  //       style('fill', '#f1f3f4').
  //       style('stroke-width', '1px').
  //       style('width', node.width + 'px');
  //   g.append('text').
  //       attr('x', node.x + 4).
  //       attr('y', node.y + 15).
  //       attr('class', 'unselectable').
  //       text(() => node.name).
  //       each(function wrap() {
  //         let self = d3.select(this),
  //             textLength = self.node().getComputedTextLength(),
  //             text = self.text();
  //         while (textLength > (node.width - 2 * 4) && text.length > 0) {
  //           text = text.slice(0, -1);
  //           self.text(text + '...');
  //           textLength = self.node().getComputedTextLength();
  //         }
  //       });
  // }
  // // body
  // let body = g.append('rect').attr('class', 'body');
  // body.style('width', node.width + 'px').
  //     style('fill', 'white').
  //     style('stroke-width', '1px');
  // if (node.type !== 'start' && node.type !== 'end') {
  //   body.attr('x', node.x).attr('y', node.y + 20);
  //   body.style('height', roundTo20(node.height - 20) + 'px');
  // } else {
  //   body.attr('x', node.x).
  //       attr('y', node.y).
  //       classed(node.type, true).
  //       attr('rx', 30);
  //   body.style('height', roundTo20(node.height) + 'px');
  // }
  // body.attr('stroke', borderColor);

  // // body text
  // let text = node.type === 'start'
  //     ? 'Start'
  //     : (node.type === 'end' ? 'End' : (
  //             (!node.approvers || node.approvers.length === 0)
  //                 ? 'No approver'
  //                 : (
  //                     node.approvers.length > 1
  //                         ? `${node.approvers[0].name + '...'}`
  //                         : node.approvers[0].name
  //                 )
  //         )
  //     );
  // let bodyTextY;
  // if (node.type !== 'start' && node.type !== 'end') {
  //   bodyTextY = node.y + 25 + roundTo20(node.height - 20) / 2;
  // } else {
  //   bodyTextY = node.y + 5 + roundTo20(node.height) / 2;
  // }
  // g.append('text').
  //     attr('x', node.x + node.width / 2).
  //     attr('y', bodyTextY).
  //     attr('class', 'unselectable').
  //     attr('text-anchor', 'middle').
  //     text(function() { return text; }).each(function wrap() {
  //   let self = d3.select(this),
  //       textLength = self.node().getComputedTextLength(),
  //       text = self.text();
  //   while (textLength > (node.width - 2 * 4) && text.length > 0) {
  //     text = text.slice(0, -1);
  //     self.text(text + '...');
  //     textLength = self.node().getComputedTextLength();
  //   }
  // });
}

export default render;
