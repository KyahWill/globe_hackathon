import { Table, TableHeader, TableRow, TableHead } from "./../components/ui/table.jsx";

const Location = () => {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Status</TableHead>
          <TableHead>Public Sentiment</TableHead>
        </TableRow>
      </TableHeader>
    </Table>
  );
};

export default Location;