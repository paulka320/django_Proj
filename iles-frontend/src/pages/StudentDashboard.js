import { useEffect, useState, useContext } from "react";
import { AuthContext } from "../auth/AuthContext";
import { getStudentLogs, getStudentPlacement, getStudentEvaluations } from "../api/student";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";
import { Card, Container, Row, Col, Table, Badge } from "react-bootstrap";

const StudentDashboard = () => {
  const { user } = useContext(AuthContext);
  const [logs, setLogs] = useState([]);
  const [placement, setPlacement] = useState(null);
  const [evaluations, setEvaluations] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const logRes = await getStudentLogs();
        setLogs(logRes.data);

        const placementRes = await getStudentPlacement();
        setPlacement(placementRes.data);

        const evalRes = await getStudentEvaluations();
        setEvaluations(evalRes.data);
      } catch (err) {
        console.log("Error fetching dashboard data:", err);
      }
    };
    fetchData();
  }, [user]);

  // Prepare data for chart
  const chartData = evaluations.map((ev, index) => ({
    week: index + 1,
    score: ev.total_score,
  }));

  // Stats
  const totalLogs = logs.length;
  const submittedLogs = logs.filter((l) => l.status === "Submitted").length;
  const pendingLogs = totalLogs - submittedLogs;
  const avgScore = evaluations.length > 0 ? (evaluations.reduce((a,b)=>a+b.total_score,0)/evaluations.length).toFixed(2) : 0;

  return (
    <Container fluid className="p-4">
      {/* Welcome Banner */}
      <Row className="mb-4">
        <Col>
          <Card className="bg-primary text-white p-3">
            <h2>Welcome, {user.username}!</h2>
            <p>Role: {user.role}</p>
          </Card>
        </Col>
      </Row>

      {/* Placement Info */}
      {placement && (
        <Row className="mb-4">
          <Col>
            <Card className="p-3">
              <h4>Current Placement</h4>
              <p><strong>Company:</strong> {placement.company_name}</p>
              <p><strong>Start Date:</strong> {placement.start_date}</p>
              <p><strong>End Date:</strong> {placement.end_date}</p>
            </Card>
          </Col>
        </Row>
      )}

      {/* Stats Cards */}
      <Row className="mb-4">
        <Col md={4}>
          <Card className="text-center p-3">
            <h5>Total Logs</h5>
            <h2>{totalLogs}</h2>
          </Card>
        </Col>
        <Col md={4}>
          <Card className="text-center p-3">
            <h5>Submitted Logs</h5>
            <h2>{submittedLogs}</h2>
          </Card>
        </Col>
        <Col md={4}>
          <Card className="text-center p-3">
            <h5>Average Score</h5>
            <h2>{avgScore}</h2>
          </Card>
        </Col>
      </Row>

      {/* Weekly Logs Table */}
      <Row className="mb-4">
        <Col>
          <Card className="p-3">
            <h4>Weekly Logs</h4>
            <Table striped bordered hover responsive>
              <thead>
                <tr>
                  <th>Week</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {logs.map((log) => (
                  <tr key={log.id}>
                    <td>{log.week_number}</td>
                    <td>
                      <Badge bg={log.status === "Submitted" ? "success" : "warning"}>
                        {log.status}
                      </Badge>
                    </td>
                  </tr>
                ))}
              </tbody>
            </Table>
          </Card>
        </Col>
      </Row>

      {/* Evaluation Chart */}
      <Row>
        <Col>
          <Card className="p-3">
            <h4>Evaluation Scores Over Weeks</h4>
            {chartData.length > 0 ? (
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={chartData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="week" label={{ value: "Week", position: "insideBottomRight", offset: 0 }} />
                  <YAxis label={{ value: "Score", angle: -90, position: "insideLeft" }} />
                  <Tooltip />
                  <Line type="monotone" dataKey="score" stroke="#8884d8" strokeWidth={3} />
                </LineChart>
              </ResponsiveContainer>
            ) : (
              <p>No evaluation data yet</p>
            )}
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default StudentDashboard;